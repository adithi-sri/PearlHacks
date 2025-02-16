import "./User.css";

function User() {
  const items = [
    "Monday - 2.5 hours",
    "Tuesday - 3.3 hours",
    "Wednesday - 4.44 hours",
    "Thursday - 1 hour",
    "Friday - 0.55 hours",
    "Saturday - 3.2 hours",
    "Sunday - 4 hours",
  ];

  return (
    <div className="profile-container">
      <h3 className="user">Jane Doe</h3>
      <p className="writingstyles">
        I am a freshman at UNC trying to find a study buddy. I am double
        majoring in neuroscience and psychology. I live on North Campus, so if
        anyone nearby is taking similar classes, please reach out!{" "}
      </p>
      <h3 className="ranking">Leaderboard Ranking: 3rd</h3>
      <h3 className="ranking">Weekly Points: 1,300</h3>
      <button className="chat">Chat</button>
      <button className="search">Search students</button>
      <h1 className="week-progress">Weekly Progress</h1>
      <ul className="week-hours">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default User;
