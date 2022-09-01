import React from 'react'

import { Provider } from 'react-redux'

import { CameinhandymanRouter } from './router/CameinhandymanRouter'

import { store } from './store/store'

export const CameinhandymanApp = () => {
  return (
    <Provider store={store}>
      <CameinhandymanRouter />
    </Provider>
  )
}
