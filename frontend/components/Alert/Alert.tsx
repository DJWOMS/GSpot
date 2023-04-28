import React, { FC, ReactNode, useEffect, useState } from 'react'
import { IconAlertCircle, IconCircleCheck, IconAlertTriangle, IconInfoCircle, IconX } from '@tabler/icons-react'
import cn from 'classnames'
import s from './Alert.module.scss'

interface AlertProps {
  type: 'danger' | 'success' | 'primary' | 'warning'
  title?: string
  message: string
  children?: ReactNode
}
const Alert: FC<AlertProps> = ({ type, title, message, children }) => {
  const [open, setOpen] = useState(true)
  const alertType = {
    danger: { className: s.alertDanger, icon: <IconAlertTriangle /> },
    success: { className: s.alertSuccess, icon: <IconCircleCheck /> },
    primary: { className: s.alertPrimary, icon: <IconInfoCircle /> },
    warning: { className: s.alertWarning, icon: <IconAlertCircle /> },
  }
  const close = () => {
    setOpen(false)
  }
  useEffect(() => {
    const time = setTimeout(() => {
      setOpen(false)
    }, 5000)
    return () => clearTimeout(time)
  }, [open])
  return (
    <div className={cn(s.alert, alertType[type].className, !open && s.alertHidden)}>
      <div className={s.alertIcon}>{alertType[type].icon}</div>
      <div className={s.alertContent}>
        <p className={s.alertContentTitle}>{title}</p>
        <p className={s.alertContentMessage}>{message}</p>
        {children}
      </div>
      <button onClick={close} className={s.alertCloseBtn}>
        <IconX />
      </button>
    </div>
  )
}

export default Alert
