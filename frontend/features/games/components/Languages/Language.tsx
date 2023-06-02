import { FC } from 'react'
import { IconCheck, IconX } from '@tabler/icons-react'
import type { LanguageInterface } from '../../types'
import s from './Language.module.css'

const Condition = (value: boolean) => (value ? <IconCheck color="green" /> : <IconX color="red" />)

const Language: FC<LanguageInterface> = ({ languageName, interfaces, subtitles, voice }) => {
  return (
    <tr>
      <th scope="row" className={s.languageName}>
        {languageName}
      </th>
      <td className={s.column}>{Condition(interfaces)}</td>
      <td className={s.column}>{Condition(subtitles)}</td>
      <td className={s.column}>{Condition(voice)}</td>
    </tr>
  )
}

export { Language }
