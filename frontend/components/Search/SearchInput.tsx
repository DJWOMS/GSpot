import { FC, Fragment } from 'react'
import { Combobox, Transition } from '@headlessui/react'
import cn from 'classnames'
import type { GameCardSimpleInterface } from 'features/games/types'
import s from './Search.module.css'

interface Props {
  onChange: (value: string) => void
  result?: GameCardSimpleInterface[]
}

const SearchInput: FC<Props> = ({ onChange, result }) => {
  return (
    <Combobox>
      <div className="relative w-full">
        <div className={s.wrapper}>
          <Combobox.Input
            placeholder={'Я ищу...'}
            className={s.combo}
            onChange={(e) => onChange(e.target.value)}
          />
        </div>

        {result && (
          <Transition
            as={Fragment}
            leave="transition ease-in duration-100"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
            afterLeave={() => onChange('')}
          >
            <Combobox.Options className={s.options}>
              {result.map((game) => (
                <Combobox.Option
                  key={game.link}
                  className={({ active }) => cn(s.option, { [s.optionActive]: active })}
                  value={game}
                >
                  <span className="block truncate font-normal">{game.title}</span>
                </Combobox.Option>
              ))}
            </Combobox.Options>
          </Transition>
        )}
      </div>
    </Combobox>
  )
}

export default SearchInput
