import { FC } from 'react'
import LogoPNG from 'assets/img/logo.png'
import Image from 'next/image'
import Link from 'next/link'
import s from './Form.module.css'

interface FormProps {
  onSubmit: (data: object) => void
  children?: React.ReactNode
}

const Form: FC<FormProps> = ({ onSubmit, children }) => {
  return (
    <div className={s.signContent}>
      <form className={s.signForm} onSubmit={onSubmit}>
        <Link className={s.signLogo} href="/">
          <Image src={LogoPNG} width={496} height={161} alt="Logo" />
        </Link>
        {children}
      </form>
    </div>
  )
}

export default Form
