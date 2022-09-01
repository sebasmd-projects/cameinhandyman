import { Route, Routes } from 'react-router-dom';
import { Error404Page } from '../site/errors/Error404Page';
import { CameinhandymanPrivateRoutes } from './CameinhandymanPrivateRoutes';
import { CaminhandymanPublicRoutes } from './CameinhandymanPublicRoutes';

export const CameinhandymanRouter = () => {
  return (
    <Routes>
      <Route path="/*" element={<CaminhandymanPublicRoutes />} />
      <Route path="p/*" element={<CameinhandymanPrivateRoutes />} />
      <Route path="*" element={<Error404Page />} />
    </Routes>
  )
}
