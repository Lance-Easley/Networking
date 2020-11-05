# Networking
This is a project that will be implemented into my repository [Uhmoung Us](https://github.com/Lance-Easley/Uhmong-Us)

I followed a tutorial made by [Tech with Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg) where he walked through a basic multiplayer game using sockets and threading.
His tutorial only supported having 2 clients connect to a server to play on. 
However, I need to have 10 players supported, so after watching through his tutorial series, I worked on expanding the supported number of clients to 10.

### **NOTE**
The project works, but there is one known bug.
Say we have 5 connected clients.
The client that connected last can leave, and the others will still be connected.
However, if the third person that connected leaves, it will either kick all other people off, or just the people that joined after that thrid person.
I believe this has something to do with my `player` dictionary, but I have not figured it out yet.
