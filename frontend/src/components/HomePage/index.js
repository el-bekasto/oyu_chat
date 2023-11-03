import ChatListChat from "../ChatListChat";

export default function HomePage () {
    const chats = [
        {
            chatId: 1,
            avatar: <img src={'https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg'}/>,
            name: "Ivan",
            lastMessage: "Hey!"
        },
        {
            chatId: 2,
            avatar: <img src={'https://pbs.twimg.com/media/FvjoUDAXoAAYiS_.jpg'}/>,
            name: "Nastya",
            lastMessage: "Good bye!"
        }
    ];
    return (
        <div className={"container"}>
            <div className={"row"} style={{marginBottom: "25px"}}>
                <h1>Chats</h1>
            </div>
            {chats.map(x => <ChatListChat chatInfo={x}/>)}
        </div>
    );
}