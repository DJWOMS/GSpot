'use client'

import { useEffect, useState } from 'react'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'
import cn from 'classnames'
import Image from 'next/image'
import { useRouter } from 'next/navigation'
import s from './CheckAge.module.css'

const CheckAge = ({ image, age }: { image: string; age: string }) => {
  const [date, setDate] = useState(new Date())
  const [isVisible, setIsVisible] = useState(true)
  const router = useRouter()

  const calculateAge = (birthMonth: number, birthDay: number, birthYear: number) => {
    const currentDate = new Date()
    const currentYear = currentDate.getFullYear()
    const currentMonth = currentDate.getMonth() + 1
    const currentDay = currentDate.getDate()
    let calculatedAge = currentYear - birthYear

    if (currentMonth < birthMonth - 1) {
      calculatedAge--
    }
    if (birthMonth - 1 == currentMonth && currentDay < birthDay) {
      calculatedAge--
    }
    return calculatedAge
  }

  const confirmAge = () => {
    const userAge = calculateAge(date.getMonth() + 1, date.getDay(), date.getFullYear())
    if (userAge < 18) {
      alert('Пожалуйста, введите корректную дату')
    } else {
      setIsVisible(false)
    }
  }

  useEffect(() => {
    if (isVisible) {
      document.body.classList.add('_lock')
    } else {
      document.body.classList.remove('_lock')
    }
  }, [isVisible])

  return (
    <>
      {age === 'adult' && (
        <div className={cn(s.wrapper, { [s.wrapperHidden]: !isVisible })}>
          <div className={s.divStyle}>
            <div className={s.imageBox}>
              <Image src={image} width={340} height={240} className={s.image} alt="" />
            </div>
            <div className={s.titleBox}>
              <div className={s.title}>
                Внимание: игра может содержать контент, не подходящий для всех возрастов или для просмотра на
                работе.
              </div>
              <form className={s.form} onSubmit={confirmAge}>
                <div className={s.tip}>Пожалуйста, укажите дату своего рождения:</div>

                <div className={s.dateBox}>
                  <DatePicker
                    className={s.input}
                    selected={date}
                    onChange={(date: Date) => setDate(date)}
                    dateFormat="dd"
                  />
                  <DatePicker
                    className={s.input}
                    selected={date}
                    onChange={(date: Date) => setDate(date)}
                    showMonthYearPicker
                    dateFormat="MMMM"
                  />
                  <DatePicker
                    className={s.input}
                    selected={date}
                    onChange={(date: Date) => setDate(date)}
                    showYearPicker
                    dateFormat="yyyy"
                  />
                </div>
              </form>
              <div className={s.btnBox}>
                <button className={s.btn} onClick={confirmAge}>
                  Открыть страницу
                </button>
                <button className={s.btn} onClick={() => router.back()}>
                  Отмена
                </button>
              </div>
            </div>
          </div>
          <footer className={s.footer}>
            <div className={s.tip}>
              Эта информация предназначена исключительно для проверки и не будет сохранена.
            </div>
          </footer>
        </div>
      )}
    </>
  )
}

export default CheckAge
