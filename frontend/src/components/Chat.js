import {useParams} from "react-router-dom";

export default function Chat ({ props }) {
    const params = useParams();
    console.log(params.id);
    return (
        <div>
            <h1>hm</h1>
            <h1>{props}</h1>
        </div>
    )
}