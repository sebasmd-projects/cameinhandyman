import { Route, Routes } from 'react-router-dom';
import { AuthRoutes } from '../site/auth/AuthRoutes';
import { DashboardPage } from '../site/dashboard/DashboardPage';
import { Error404Page } from '../site/helpers/errors/Error404Page';
import { FAQPage } from '../site/faq/FAQPage';
import { ServicesPage } from '../site/services/ServicesPage';


export const CaminhandymanPublicRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<DashboardPage title="Came in Handyman - Home" />} />
      <Route path="/contact" element={<ServicesPage title="Came in Handyman - Contact" />} />
      <Route path="/faq" element={<FAQPage title="Came in Handyman - FAQ" />} />
      <Route path="/services" element={<ServicesPage title="Came in Handyman - Services" />} />
      <Route path="user/auth/*" element={<AuthRoutes />} />
      <Route path="*" element={<Error404Page />} />
    </Routes>
  )
}
