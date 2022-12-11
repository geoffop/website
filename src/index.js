import initScrollReveal from "./scripts/scrollReveal";
import initTiltEffect from "./scripts/tiltAnimation";
import {targetElements, defaultProps} from "./data/scrollRevealConfig";
import "@fortawesome/fontawesome-free/css/all.css"; 

initScrollReveal(targetElements, defaultProps);
initTiltEffect();
