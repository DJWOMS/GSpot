import React, { FC, ReactNode, useEffect, useRef, useState } from 'react'
import {
  IconAlertCircle,
  IconCircleCheck,
  IconAlertTriangle,
  IconInfoCircle,
  IconX,
} from '@tabler/icons-react'
import cn from 'classnames'
import s from './Alert.module.css'

interface AlertProps {
  type: 'danger' | 'success' | 'primary' | 'warning'
  title?: string
  message: string
  duration?: number
  closable?: boolean
  children?: ReactNode
}
const Alert: FC<AlertProps> = ({ type, title, message, closable, duration, children }) => {
  const [open, setOpen] = useState(true)
  const dismissRef = useRef<ReturnType<typeof setTimeout>>()
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
    if (duration) {
      dismissRef.current = setTimeout(() => {
        setOpen(false)
      }, duration * 1000)
    }
    return () => clearTimeout(dismissRef.current)
  }, [duration])
  return (
    <>
      {open ? (
        <div className={cn(s.alert, alertType[type].className)}>
          <div className={s.alertIcon}>{alertType[type].icon}</div>
          <div className={s.alertContent}>
            <p className={s.alertContentTitle}>{title}</p>
            <p className={s.alertContentMessage}>{message}</p>
            {children}
          </div>
          {closable && (
            <button onClick={close} className={s.alertCloseBtn}>
              <IconX />
            </button>
          )}
        </div>
      ) : null}
    </>
  )
}

export default Alert
