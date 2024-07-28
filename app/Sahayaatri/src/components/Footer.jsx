import instagram from "../assets/instagram-dark.png";
import twitter from "../assets/twitter-dark.png";
import whatsapp from "../assets/whatsapp-dark.png";

function Footer() {
    return (
        <footer className="footer">
            <p>Sahayaatri, your travel guide.</p>
            <div>
                <img src={instagram}></img>
                <img src={twitter}></img>
                <img src={whatsapp}></img>
            </div>
        </footer>
    )
}

export default Footer;
