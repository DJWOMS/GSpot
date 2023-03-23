import { useState } from 'react'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'
import './styles.css'

const Bday = (): JSX.Element => {
    const [startDay, setStartDay] = useState(new Date())
    const [starMonth, setStarMonth] = useState(new Date())
    const [startYear, setStartYear] = useState(new Date())
    return (
        <div className="flex flex-row gap-2 justify-center w-fit pt-4">
            <DatePicker
                className="bday lg:w-10 w-8 lg:text-xl text-xs"
                selected={startDay}
                onChange={(date: Date) => setStartDay(date)}
                dateFormat="dd"
            />
            <DatePicker
                className="bday lg:w-24 w-14"
                selected={starMonth}
                onChange={(date: Date) => setStarMonth(date)}
                showMonthYearPicker
                dateFormat="MMMM"
            />
            <DatePicker
                className="bday lg:w-20 w-10"
                selected={startYear}
                onChange={(date: Date) => setStartYear(date)}
                showYearPicker
                dateFormat="yyyy"
            />
        </div>
    )
}

export default Bday
