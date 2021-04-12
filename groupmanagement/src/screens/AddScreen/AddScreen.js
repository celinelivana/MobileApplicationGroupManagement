import React, { useState } from 'react'
import {Alert,StyleSheet,SafeAreaView,Text, View,TouchableOpacity, TextInput} from 'react-native'
import colors from '../../../assets/colors/colors'
import { connect } from 'react-redux'
import { useNavigation } from '@react-navigation/native';
import axios from 'axios'
import AsyncStorage from '@react-native-async-storage/async-storage';

// ini diganti fab
const AddScreen = (user) => {
    const navigation = useNavigation();

    const status = ""
    const [Group, setGroup] = useState()
    const [Description, setDesc] = useState()

    const addGroup = async() => {
        try{
        let token = await AsyncStorage.getItem('token');  
        const data = {
            name: Group, 
            description: Description, 
            owner: user.user.studentID
          }
        const submit = await axios.post(`http://192.168.100.246:8000/api/group/create/`, data, {
            headers:{
              'Authorization': 'JWT ' + token,
          }
      })
    //   .then(resp=>{
    //     // status = resp.status
    // })
      console.log(submit.data)
    //   navigation.navigate('Main')
    }catch{

    }
    }
    return (
        <SafeAreaView style={styles.view1}>
            <View style>
        <Text style={styles.Text}>Upload Your Project Proposal Here</Text>
        </View>
        <View style = {styles.content}>
        <Text style={styles.label}>Group Name:</Text>
        <TextInput
                    style={{
                        borderRadius: 8,
                        borderWidth: 1,
                        width: 300,
                        margin: 5,
                        fontFamily: "Roboto-Regular",
                        fontSize: 15
                    }}
                    placeholder="Group"
                    placeholderTextColor='grey'
                    backgroundColor='white'
                    onChangeText={text => setGroup(text)}
                />
        <Text style={styles.label}>Description:</Text>
        <TextInput
                    style={{height:100,
                        borderRadius: 8,
                        borderWidth: 1,
                        width: 300,
                        margin: 5,
                        fontFamily: "Roboto-Regular",
                        fontSize: 15}}
                    placeholder="Description..."
                    placeholderTextColor='grey'
                    backgroundColor='white'
                    multiline={true}
                    scrollEnabled ={true}
                    editable={true}
                    returnKeyType='next'
                    onChangeText={text => setDesc(text)}
                />       
                <TouchableOpacity
                    style={Group && Description != null ? styles.loginButton : styles.loginButtonBlocked}
                    onPress={() => addGroup()}
                    disabled={Group && Description != null ?  false : true}
                >
                    <Text>Upload</Text>
                </TouchableOpacity> 
            </View>                        
        </SafeAreaView>
    )
}
const styles = StyleSheet.create({
    Text: {
        fontSize: 20,
        color:'orange',
        borderRadius:8,
        backgroundColor:'white',
        textAlign:'center',
        padding: 5,
        marginTop:25,
        marginLeft: 18,
        width: '90%',

    },
    content:{
        marginTop: 15,
        padding: 10,
        alignItems:'center'
    },
    label:{
        fontSize:15,
       color:'white',
       fontWeight:'bold'
    },
    view1:{
        backgroundColor: 'orange',
        flex :1,
    },   loginButton: {
        alignItems: 'center',
        padding: 10,
        width: 200,
        margin: 15,
        borderRadius: 5,
        backgroundColor: colors.lightYellow
    },
    loginButtonBlocked: {
        alignItems: 'center',
        padding: 10,
        width: 200,
        margin: 15,
        borderRadius: 5,
        backgroundColor: colors.textLight
    },
    textinput: {
        borderRadius: 5,
        borderWidth: 1,
        width: 300,
        margin: 5,
        fontFamily: "Roboto-Regular",
        fontSize: 20
    },
    Button: {
        alignItems: 'center',
        padding: 10,
        width: 200,
        margin: 15,
        borderRadius: 5,
        backgroundColor: colors.lightYellow
    },
})

const mapStateToProps = (state) => ({
    user: state.auth.user
  })
export default connect(mapStateToProps, null)(AddScreen)