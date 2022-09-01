import ReactDOM from 'react-dom/client';

import { BrowserRouter as Router } from 'react-router-dom';

import { CameinhandymanApp } from './CameinHandyManApp';

import './main.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <CameinhandymanApp />
  </Router>
);