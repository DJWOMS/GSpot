import { FC } from 'react'
import { LanguageInterface } from 'features/games'
import { Language } from './Language'

type LanguagesProps = {
  children: LanguageInterface[]
}

const Languages: FC<LanguagesProps> = ({ children }) => {
  return (
    <table className="text-center text-sm">
      <thead className="text-xs uppercase">
        <tr>
          <th scope="col">Язык</th>
          <th scope="col" className="px-6 py-3">
            Интерфейс
          </th>
          <th scope="col" className="px-6 py-3">
            Озвучка
          </th>
          <th scope="col" className="px-6 py-3">
            Субтитры
          </th>
        </tr>
      </thead>
      <tbody>
        {children.map((language) => (
          <Language key={language.languageName} {...language} />
        ))}
      </tbody>
    </table>
  )
}

export { Languages }
