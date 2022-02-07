import "./2d.css"

export const DiceSVG = (props) => {
    let dieType = "";

    switch (props.sides) {
        case "4":
            dieType = <polygon points="125,0 0,200 250,200" rx="50" ry="50" fill="#bfbeb0" strokeWidth="0" />
            break;

        case "6":
            dieType = <rect width="250" height="250" rx="50" ry="50" fill="#bfbeb0" strokeWidth="0" />
            break;

        case "8":
            dieType = <polygon points="125,0 250,125 125,250 0,125" rx="50" ry="50" fill="#bfbeb0" strokeWidth="0" />
            break;

        case "10":
            dieType = <rect width="250" height="250" rx="50" ry="50" fill="#bfbeb0" strokeWidth="0" />
            break;

        case "12":
            dieType = <rect width="250" height="250" rx="50" ry="50" fill="#bfbeb0" strokeWidth="0" />
            break;

        case "20":
            dieType = <rect width="250" height="250" rx="50" ry="50" fill="#bfbeb0" strokeWidth="0" />
            break;

        default:
            <></>
    }

    return (
        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
        viewBox="0 0 250 250" style={{enableBackground: "new 0 0 120 120"}}>
            {dieType}
            <text x="50%" y="50%"
                dominantBaseline="middle"
                textAnchor="middle"
                style={{ font: "bold 60px sans-serif" }}
            >
                {props.value}
            </text>
        </svg>
    );
}

export default DiceSVG; 