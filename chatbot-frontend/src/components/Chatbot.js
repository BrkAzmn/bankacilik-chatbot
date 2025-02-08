import React, { useState, useRef, useEffect } from "react";

const Chatbot = () => {
    const [query, setQuery] = useState("");
    const [messages, setMessages] = useState(() => {
        const savedMessages = localStorage.getItem("chatHistory");
        return savedMessages ? JSON.parse(savedMessages) : [];
    });
    const [isTyping, setIsTyping] = useState(false);

    const chatBoxRef = useRef(null);
    const userId = "user123"; // Kullanıcı kimliği

    useEffect(() => {
        if (chatBoxRef.current) {
            chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
        }
    }, [messages, isTyping]);

    useEffect(() => {
        localStorage.setItem("chatHistory", JSON.stringify(messages));
    }, [messages]);

    const sendMessage = async (userInput) => {
        if (!userInput.trim()) return;

        const userMessage = { sender: "user", text: userInput };
        setMessages((prevMessages) => [...prevMessages, userMessage]);

        setQuery("");
        setIsTyping(true);

        try {
            const response = await fetch(`http://127.0.0.1:8000/chatbot/?user_id=${userId}&query=${encodeURIComponent(userInput)}`);
            const data = await response.json();
            const botMessage = { sender: "bot", text: data.response, emotion: data.emotion };

            setMessages((prevMessages) => [...prevMessages, botMessage]);
        } catch (error) {
            setMessages((prevMessages) => [...prevMessages, { sender: "bot", text: "Hata: API'ye bağlanılamadı.", emotion: "Bilinmiyor" }]);
        }

        setIsTyping(false);
    };

    return (
        <div className="chat-container">
            <div className="chat-header">
                💬 Banka Chatbot
            </div>
            <div className="chat-box" ref={chatBoxRef}>
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        {msg.text}
                        {msg.sender === "bot" && msg.emotion && (
                            <div className="emotion-tag">{msg.emotion}</div>
                        )}
                    </div>
                ))}
                {isTyping && (
                    <div className="message bot typing-indicator">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                )}
            </div>
            <div className="suggested-questions">
                <p>🔹 Sık Sorulan Sorular:</p>
                <button onClick={() => sendMessage("Kredi kartı başvurusu nasıl yapılır?")}>💳 Kredi Kartı Başvurusu</button>
                <button onClick={() => sendMessage("IBAN numaramı nasıl öğrenebilirim?")}>🏦 IBAN Bilgisi</button>
                <button onClick={() => sendMessage("Banka havale işlemi nasıl yapılır?")}>💸 Havale İşlemi</button>
                <button onClick={() => sendMessage("Güncel faiz oranlarını öğrenebilir miyim?")}>📊 Faiz Oranları</button>
            </div>
            <div className="input-box">
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Sorunuzu yazın..."
                />
                <button onClick={() => sendMessage(query)}>Gönder</button>
            </div>
        </div>
    );
};

export default Chatbot;
