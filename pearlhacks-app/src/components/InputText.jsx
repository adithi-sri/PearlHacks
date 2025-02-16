import React from "react";

const InputText = ({addMessage}) => {
    const[message, setMessage] = useState()
    const sendMessage = () => {
        addMessage({message})
        setMessage("")
    }
    return (
        <div className="inputtext_container">
            <textarea name="message" id="message" rows="6" placeholder = "Input Message"
            onChange = {(e) => setMessage(e.target.value)}></textarea>
            <button>onClick = {() => sendMessage}</button>
        </div>
    );
};

export default InputText;