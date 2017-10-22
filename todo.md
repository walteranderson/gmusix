[x] authenticate client with gmusic API
[ ] create a room with multiple clients
[ ] each client requests the stream url
    - steam url defined by the room, managed by the host
[x] use [react-sound](https://www.npmjs.com/package/react-sound) to play back audio
    - use as a controlled component and send back messages to the server about position/duration
    - need to figure out how to buffer the entire mp3 before stream URL expires
[ ] server manages each client's position in the song and makes sure they stay syncronized
