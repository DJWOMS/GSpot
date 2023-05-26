'use client'

import { FC, useState } from 'react'
import type { LanguageInterface } from '../../types'
import { Language } from './Language'

type LanguagesProps = {
  children: LanguageInterface[]
}

const Languages: FC<LanguagesProps> = ({ children }) => {
  const [allLanguagesOpen, setAllLanguagesOpen] = useState(false)
  return (
    <>
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
          {allLanguagesOpen
            ? children.map((language) => <Language key={language.languageName} {...language} />)
            : children.slice(0, 2).map((language) => <Language key={language.languageName} {...language} />)}
        </tbody>
      </table>
      {children.length > 2 && (
        <button
          onClick={() => setAllLanguagesOpen(!allLanguagesOpen)}
          className="whitespace-nowrap font-medium text-primary"
        >
          {allLanguagesOpen ? 'Свернуть' : 'Показать все'}
        </button>
      )}
    </>
  )
}

export default Languages
