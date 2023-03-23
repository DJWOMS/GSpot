import './styles.css'
import Bday from './Bday'

const CheckAge = () => {
    return (
        <div className="mainBlock">
            <div className="divStyle lg:p-44 lg:pb-10 pb-10 p-2">
                <div className="md:h-1/3 h-1/4 lg:w-1/4 w-2/4 absolute -top-10">
                    <img alt="Game image" src="https://picsum.photos/1000" className="styleImg" />
                </div>
                <div className="flex flex-col lg:w-4/5 w-11/12 h-full items-center justify-center contain ">
                    <h1 className="styleH1 md:text-xl text-xs lg:pt-4 pt-10">
                        ВНИМАНИЕ: ИГРА МОЖЕТ СОДЕРЖАТЬ КОНТЕНТ, НЕ ПОДХОДЯЩИЙ ДЛЯ ВСЕХ ВОЗРАСТОВ ИЛИ ДЛЯ ПРОСМОТРА НА РАБОТЕ.
                    </h1>
                    <form className="styleForm md:text-xl text-xs">
                        <p>Пожалуйста, укажите дату своего рождения:</p>
                        <Bday />
                    </form>
                    <div className="flex flex-row gap-3 w-full justify-center mt-6">
                        <button className="btn lg:text-xl text-xs">Открыть страницу</button>
                        <button className="btn lg:text-xl text-xs">Отмена</button>
                    </div>
                </div>
            </div>
            <footer className="footer">
                <p className="md:text-xl text-xs">Эта информация предназначена исключительно для проверки и не будет сохранена.</p>
            </footer>
        </div>
    )
}

export default CheckAge
