# 🎵 Musical Time Machine 
A Python project that lets you travel back in time through music! Enter any date, and the app will fetch the **Billboard Hot 100 songs** from that day and create a **Spotify playlist** with those tracks. 

--- 

## ✨ Features 
- ⏳ Travel back to any date in music history
- 🎶 Automatically fetches the Billboard Hot 100 songs
- 📀 Creates a Spotify playlist instantly
- 🪄 Simple and fun way to rediscover music

--- 

## 🎥 Demo Video 

https://github.com/user-attachments/assets/faab8935-1bd2-4c6b-9420-b911b5d59a95

---

## 📸 Screenshot 
<img width="1470" height="956" alt="Screenshot 2025-08-24 at 4 52 49 PM" src="https://github.com/user-attachments/assets/618eeeb3-d92e-47ea-b7b0-10748bed54fb" />

--- 

## ⚙️ Installation 
1. Clone the repository:
``` bash 
   git clone https://github.com/bhavikakeswani/musical-time-machine.git
   cd musical-time-machine
   ```
3. Install dependencies:
``` bash 
   pip install -r requirements.txt
   ```
4. Create a .env file and add your Spotify API credentials:
``` bash 
   SPOTIPY_CLIENT_ID=your_client_id
  SPOTIPY_CLIENT_SECRET=your_client_secret
  SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
   ```

--- 

## 🚀 Usage 
1. Run the script:
``` bash 
   python main.py
   ```
2. Enter a date in the format:
``` bash 
   YYYY-MM-DD
   ```
3. The program will:
- Fetch Billboard Hot 100 songs from that date
- Create a Spotify playlist in your account

## 📦 Requirements 
See [requirements.txt](requirements.txt). 

---

### License 
This project is licensed under the [MIT License](LICENSE). 

---
