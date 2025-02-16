import "./Leaderboard.css";

function Leaderboard() {
  const items = [
    "1st Place",
    "2nd Place",
    "3rd Place",
    "4th Place",
    "5th Place",
    "6th Place",
    "7th Place",
    "8th Place",
    "9th Place",
    "10th Place",
  ];
  return (
    <body className="container">
      <h1 className="led">Leaderboard</h1>
      <ul className="list-group">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </body>
  );
}

export default Leaderboard;
