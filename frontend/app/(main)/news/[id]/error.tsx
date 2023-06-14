'use client'

import React from 'react'
import Error from 'components/Error/error'

const ErrorProfile = ({ reset }: { reset: () => void }) => {
  return <Error reset={reset} textError={'Ошибка'} />
}

export default ErrorProfile
