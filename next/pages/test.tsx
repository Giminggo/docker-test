import { atom } from "recoil";
import { useRecoilState } from "recoil";
import { RefObject, useRef, useState } from "react";

const testKey = atom({
  key: 'testKey',
  default: undefined
})

export default function Test() {

  const inputRef = useRef<RefObject<HTMLInputElement>>(null);

  const [state, setState] = useState(false);

  const [test, setTest] = useRecoilState(testKey)

  console.log(test);

  const loadDjango = async() => {
    let response = await fetch(`http://localhost:8090/api/test/${inputRef.current.value}/`);
    if (response.status === 200){
      setState(true);
    }

  }

  return (
    <>
      <h1>hello World</h1>
      <span>이름을 입력해주세요</span>
      <input ref={inputRef}></input>
      <button onClick={loadDjango}>API Test</button>
      {state && <span>API테스트 성공</span>}
    </>
  )
}