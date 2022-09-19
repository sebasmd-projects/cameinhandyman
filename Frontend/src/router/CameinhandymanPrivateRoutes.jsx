import { Route, Routes } from 'react-router-dom';
import { BookingPage } from '../site/pages/booking/BookingPage';
import { Error404Page } from '../site/helpers/errors/Error404Page';

export const CameinhandymanPrivateRoutes = () => {
  return (
    <Routes>
      <Route path="booking" element={<BookingPage title="Came in Handyman - Booking" />} />
      <Route path="*" element={<Error404Page />} />
    </Routes>
  )
}
