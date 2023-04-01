import { FC } from 'react'
import { IconCheck, IconX } from '@tabler/icons-react'
import { LanguageInterface } from 'features/games'

const Condition = (value: boolean) => (value ? <IconCheck color="green" /> : <IconX color="red" />)

const Language: FC<LanguageInterface> = ({ languageName, interfaces, subtitles, voice }) => {
  return (
    <tr>
      <th scope="row" className="py-4 font-medium">
        {languageName}
      </th>
      <td className="px-6 py-4">{Condition(interfaces)}</td>
      <td className="px-6 py-4">{Condition(subtitles)}</td>
      <td className="px-6 py-4">{Condition(voice)}</td>
    </tr>
  )
}

export { Language }
