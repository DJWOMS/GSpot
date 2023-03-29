import { FC, Fragment } from 'react'
import { Combobox, Transition } from '@headlessui/react'
import s from './Search.module.scss'
import cn from 'classnames'

interface ICategory {
  id: number
  name: string
}

interface Props {
  onChange: (value: string) => void
  result: ICategory[]
}

const SearchInput: FC<Props> = ({ onChange, result }) => {
  return (
    <Combobox>
      <div className="relative">
        <div className={s.wrapper}>
          <Combobox.Input placeholder={'Я ищу...'} className={s.combo} onChange={(e) => onChange(e.target.value)} />
        </div>
        <Transition as={Fragment} leave="transition ease-in duration-100" leaveFrom="opacity-100" leaveTo="opacity-0" afterLeave={() => onChange('')}>
          <Combobox.Options className={s.options}>
            {result.map((category) => (
              <Combobox.Option key={category.id} className={({ active }) => cn(s.option, { [s.optionActive]: active })} value={category}>
                <span className="block truncate font-normal">{category.name}</span>
              </Combobox.Option>
            ))}
          </Combobox.Options>
        </Transition>
      </div>
    </Combobox>
  )
}

export default SearchInput
