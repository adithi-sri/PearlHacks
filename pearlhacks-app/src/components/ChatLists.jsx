import React from "react";

const ChatLists = ({chats}) => {
    const user = localStorage.getItem('user')
    function SenderChat(message, username, avatar){ 
        reutrn (
            <div>
                <p>
                    <strong>{username}</strong>
                    {message}
                </p>
            </div>
        )
    }
    function ReceiverChat(message, username, avatar){
        return (
            <div>
                <p>
                    <strong>{username}</strong>
                    {message}
                </p>
            </div>
        )   
    }
    return (
        <div className = 'chats_list'>
            {chats.map((chat, index) => {
                if (chat.user == user){
                    return <SenderChat
                    key = {index}
                    message = {chat.message}
                    username = {chat.user}
                    avatar = {chat.avatar}/>
                }
                return <ReceiverChat
                    key = {index}
                    message = {chat.message}
                    username = {chat.user}
                    avatar = {chat.avatar}/>
            })}
            
            <ReceiverChat />
        </div>
    )
}

export default ChatLists;