import React, {useState} from 'react';

export default function App() {
  const [users, setUsers] = useState<any>(false);

  const showUser = async() => {
    const response = await fetch('http://localhost:5050/api/users/');
    const data = await response.json();
    setUsers(data);
  };

  return (
    <>
      {users ? <h1>User Information</h1> : <h1>Show User Information</h1> }
      <br></br>
      {typeof(users) !== 'object' ? <button onClick={showUser}>전체 유저 보기</button> : users.map((user:any, index:any) => {
        return <div key={index}>
          <h1>{user.username}</h1>
          <h1>{user.age}</h1>
          <h1>{user.information}</h1>
          <br></br>
        </div>
        }
      )}
    </>
  );
}
