import { useState } from 'react'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'
import cn from 'classnames'
import Image from 'next/image'
import styles from './CheckAge.module.scss'

const CheckAge = () => {
  const [startDay, setStartDay] = useState(new Date())
  const [starMonth, setStarMonth] = useState(new Date())
  const [startYear, setStartYear] = useState(new Date())

  return (
    <div className={styles.mainBlock}>
      <div className={cn(styles.divStyle, 'p-2 pb-10 lg:p-44 lg:pb-10')}>
        <div className={cn('h-1/4 w-2/4 md:h-1/3 lg:w-1/4', styles.divImg)}>
          <Image alt="Game image" src="https://loremflickr.com/320/240" className={styles.styleImg} />
        </div>
        <div className={cn(styles.divH1, 'w-11/12 lg:w-4/5')}>
          <h1 className={cn(styles.styleH1, 'pt-10 text-xs md:text-xl lg:pt-4')}>
            ВНИМАНИЕ: ИГРА МОЖЕТ СОДЕРЖАТЬ КОНТЕНТ, НЕ ПОДХОДЯЩИЙ ДЛЯ ВСЕХ ВОЗРАСТОВ ИЛИ ДЛЯ ПРОСМОТРА НА РАБОТЕ.
          </h1>
          <form className={cn(styles.styleForm, 'text-xs md:text-xl')}>
            <p className={styles.p}>Пожалуйста, укажите дату своего рождения:</p>

            <div className={styles.divDatePicker}>
              <DatePicker
                className={cn(styles.bday, 'w-8 text-xs lg:w-10 lg:text-xl')}
                selected={startDay}
                onChange={(date: Date) => setStartDay(date)}
                dateFormat="dd"
              />
              <DatePicker
                className={cn(styles.bday, 'w-14 lg:w-24')}
                selected={starMonth}
                onChange={(date: Date) => setStarMonth(date)}
                showMonthYearPicker
                dateFormat="MMMM"
              />
              <DatePicker
                className={cn(styles.bday, 'w-10 lg:w-20')}
                selected={startYear}
                onChange={(date: Date) => setStartYear(date)}
                showYearPicker
                dateFormat="yyyy"
              />
            </div>
          </form>
          <div className={styles.divBtn}>
            <button className={cn(styles.btn, 'text-xs lg:text-xl')}>Открыть страницу</button>
            <button className={cn(styles.btn, 'text-xs lg:text-xl')}>Отмена</button>
          </div>
        </div>
      </div>
      <footer className={styles.footer}>
        <p className={cn(styles.p, 'text-xs md:text-xl')}>Эта информация предназначена исключительно для проверки и не будет сохранена.</p>
      </footer>
    </div>
  )
}

export default CheckAge
