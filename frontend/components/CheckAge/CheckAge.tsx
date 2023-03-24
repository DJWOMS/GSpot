import styles from './CheckAge.module.scss'
import cn from 'classnames'
import { useState } from 'react'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'

const CheckAge = () => {
    const [startDay, setStartDay] = useState(new Date())
    const [starMonth, setStarMonth] = useState(new Date())
    const [startYear, setStartYear] = useState(new Date())

    return (
        <div className={styles.mainBlock}>
            <div className={cn(styles.divStyle, 'lg:p-44 lg:pb-10 pb-10 p-2')}>
                <div className={cn('md:h-1/3 h-1/4 lg:w-1/4 w-2/4', styles.divImg)}>
                    <img alt="Game image" src="https://picsum.photos/1000" className={styles.styleImg} />
                </div>
                <div className={cn(styles.divH1, 'lg:w-4/5 w-11/12')}>
                    <h1 className={cn(styles.styleH1, 'md:text-xl text-xs lg:pt-4 pt-10')}>
                        ВНИМАНИЕ: ИГРА МОЖЕТ СОДЕРЖАТЬ КОНТЕНТ, НЕ ПОДХОДЯЩИЙ ДЛЯ ВСЕХ ВОЗРАСТОВ ИЛИ ДЛЯ ПРОСМОТРА НА РАБОТЕ.
                    </h1>
                    <form className={cn(styles.styleForm, 'md:text-xl text-xs')}>
                        <p className={styles.p}>Пожалуйста, укажите дату своего рождения:</p>

                        <div className={styles.divDatePicker}>
                            <DatePicker
                                className={cn(styles.bday, 'lg:w-10 w-8 lg:text-xl text-xs')}
                                selected={startDay}
                                onChange={(date: Date) => setStartDay(date)}
                                dateFormat="dd"
                            />
                            <DatePicker
                                className={cn(styles.bday, 'lg:w-24 w-14')}
                                selected={starMonth}
                                onChange={(date: Date) => setStarMonth(date)}
                                showMonthYearPicker
                                dateFormat="MMMM"
                            />
                            <DatePicker
                                className={cn(styles.bday, 'lg:w-20 w-10')}
                                selected={startYear}
                                onChange={(date: Date) => setStartYear(date)}
                                showYearPicker
                                dateFormat="yyyy"
                            />
                        </div>
                    </form>
                    <div className={styles.divBtn}>
                        <button className={cn(styles.btn, 'lg:text-xl text-xs')}>Открыть страницу</button>
                        <button className={cn(styles.btn, 'lg:text-xl text-xs')}>Отмена</button>
                    </div>
                </div>
            </div>
            <footer className={styles.footer}>
                <p className={cn(styles.p, 'md:text-xl text-xs')}>Эта информация предназначена исключительно для проверки и не будет сохранена.</p>
            </footer>
        </div>
    )
}

export default CheckAge
