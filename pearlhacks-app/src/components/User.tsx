import "./User.css";

function User() {
  return (
    <div className="profile-container">
      <h3 className="user">Jane Doe</h3>
      <p className="writingstyles">
        I am a freshman at UNC trying to find a study buddy. I am double
        majoring in neuroscience and psychology. I live on North Campus, so if
        anyone nearby is taking similar classes, please reach out!{" "}
      </p>
      <h3 className="ranking">Leaderboard Ranking: 3rd</h3>
    </div>
  );
}

export default User;
