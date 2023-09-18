import { FC } from 'react'
import { IconMailOpened } from '@tabler/icons-react'
import s from './Subscribe.module.css'

const Subscribe: FC = () => {
  return (
    <form action="#" className={s.subscribe}>
      <div className={s.image}>
        <IconMailOpened />
      </div>
      <h4 className={s.title}>Subscribe to news</h4>
      <p className={s.text}>All the Lorem Ipsum generators on the Internet tend to r chunks as necessary.</p>
      <input type="text" className={s.input} placeholder="Email" />
      <button type="button" className={s.button}>
        Send
      </button>
    </form>
  )
}

export default Subscribe
