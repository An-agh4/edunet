document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.chat-form');
    const chatMessages = document.getElementById('chat-messages');

    // Function to add a message to the chat
    function addMessage(content, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = content;

        messageDiv.appendChild(messageContent);
        chatMessages.appendChild(messageDiv);

        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Function to show typing indicator
    function showTyping() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message';
        typingDiv.id = 'typing-indicator';

        const typingContent = document.createElement('div');
        typingContent.className = 'message-content';
        typingContent.innerHTML = '<em>Typing...</em>';

        typingDiv.appendChild(typingContent);
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Function to remove typing indicator
    function hideTyping() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent default form submission

        const promptInput = document.querySelector('input[name="prompt"]');
        const prompt = promptInput.value.trim();

        if (!prompt) {
            return;
        }

        // Add user message to chat
        addMessage(prompt, true);

        // Clear input
        promptInput.value = '';

        // Show typing indicator
        showTyping();

        // Make POST request to /chat/ endpoint
        fetch('/chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                'prompt': prompt
            })
        })
        .then(response => response.json())
        .then(data => {
            hideTyping(); // Remove typing indicator

            if (data.response) {
                addMessage(data.response, false);
            } else if (data.error) {
                addMessage('Error: ' + data.error, false);
            } else {
                addMessage('Unexpected response from server.', false);
            }
        })
        .catch(error => {
            hideTyping(); // Remove typing indicator
            console.error('Error:', error);
            addMessage('An error occurred while processing your request.', false);
        });
    });
});