import { Route, Routes } from 'react-router-dom';
import { AuthLoginPage } from './AuthLoginPage';
import { AuthRegisterPage } from './AuthRegisterPage';


export const AuthRoutes = () => {
  return (

    <Routes>
      <Route path="register" element={<AuthRegisterPage title="Came in Handyman - User Register" />} />
      <Route path="login" element={<AuthLoginPage title="Came in Handyman - User Login" />} />
      <Route path="*" element={<AuthLoginPage title="Came in Handyman - User Login" />} />
    </Routes>
  )
}
