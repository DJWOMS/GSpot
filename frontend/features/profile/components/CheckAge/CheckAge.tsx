'use client'

import { useState } from 'react'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'
import Image from 'next/image'
import { useRouter } from 'next/router'
import s from './CheckAge.module.scss'

const CheckAge = (image: any, checkAge: any) => {
  const [date, setDate] = useState(new Date())
  const router = useRouter()

  const calculateAge = (birthMonth: any, birthDay: any, birthYear: any) => {
    const currentDate = new Date()
    const currentYear = currentDate.getFullYear()
    const currentMonth = currentDate.getMonth()
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
    const userAge = calculateAge(date.getMonth(), date.getDay(), date.getFullYear())
    if (userAge < 18) {
      console.log('error!')
    } else {
      changeAge()
    }
  }

  return (
    <div className={s.mainBlock}>
      <div className={s.divStyle}>
        <div className={s.divImg}>
          <Image alt="" src={image} width={340} height={240} className={s.styleImg} />
        </div>
        <div className={s.divH1}>
          <div className={s.styleH1}>ВНИМАНИЕ: ИГРА МОЖЕТ СОДЕРЖАТЬ КОНТЕНТ, НЕ ПОДХОДЯЩИЙ ДЛЯ ВСЕХ ВОЗРАСТОВ ИЛИ ДЛЯ ПРОСМОТРА НА РАБОТЕ.</div>
          <form className={s.styleForm} onSubmit={confirmAge}>
            <div className={s.p}>Пожалуйста, укажите дату своего рождения:</div>

            <div className={s.divDatePicker}>
              <DatePicker className={s.bday} selected={date} onChange={(date: Date) => setDate(date)} dateFormat="dd" />
              <DatePicker className={s.bday} selected={date} onChange={(date: Date) => setDate(date)} showMonthYearPicker dateFormat="MMMM" />
              <DatePicker className={s.bday} selected={date} onChange={(date: Date) => setDate(date)} showYearPicker dateFormat="yyyy" />
            </div>
          </form>
          <div className={s.divBtn}>
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
        <div className={s.p}>Эта информация предназначена исключительно для проверки и не будет сохранена.</div>
      </footer>
    </div>
  )
}

export { CheckAge }
