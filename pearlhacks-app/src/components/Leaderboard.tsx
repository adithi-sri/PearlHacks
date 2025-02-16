import "./Leaderboard.css";

function Leaderboard() {
  const items = [
    "1st Place - Jane Smith",
    "2nd Place - George Washington",
    "3rd Place - Jane Doe",
    "4th Place - Anonymous Cat",
    "5th Place - Anonymous Dog",
    "6th Place - Anonymous Mouse",
    "7th Place - Anonymous Orange",
    "8th Place - Thomas Jefferson",
    "9th Place - Barthalamue Johnson",
    "10th Place - Anonymous Lemur",
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
