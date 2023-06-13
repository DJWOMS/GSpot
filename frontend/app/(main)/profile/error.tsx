'use client'

import React from 'react'
import Error from '../../../components/Error/error'

const ErrorProfile = ({ reset }: { reset: () => void }) => {
  return (
    <div>
      <Error reset={reset} textError={'Ошибка настроек'} />
    </div>
  )
}

export default ErrorProfile
