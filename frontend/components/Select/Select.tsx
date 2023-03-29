import { FC, Fragment } from 'react'
import { Listbox, Transition } from '@headlessui/react'
import cn from 'classnames'
import s from './Select.module.scss'

interface Item {
  id: number
  name: string
  unavailable?: boolean
}

interface Props {
  selected?: Item
  setSelected: (value: Item) => void
  options: Item[]
}

const Select: FC<Props> = ({ selected, setSelected, options }) => {
  return (
    <Listbox value={selected} onChange={setSelected}>
      <div className="relative w-full">
        <Listbox.Button className={s.select}>
          <span className="block truncate">{selected?.name}</span>
        </Listbox.Button>
        <Transition as={Fragment} leave="transition ease-in duration-100" leaveFrom="opacity-100" leaveTo="opacity-0">
          <Listbox.Options className={s.options}>
            {options.map((item) => (
              <Listbox.Option key={item.id} className={({ active }) => cn(s.option, { [s.optionActive]: active })} value={item}>
                {({ selected }) => <span className={`block truncate ${selected ? 'font-medium' : 'font-normal'}`}>{item.name}</span>}
              </Listbox.Option>
            ))}
          </Listbox.Options>
        </Transition>
      </div>
    </Listbox>
  )
}

export default Select
