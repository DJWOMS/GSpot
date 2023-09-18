import { FC, Fragment } from 'react'
import { Listbox, Transition } from '@headlessui/react'
import cn from 'classnames'
import s from './Select.module.css'

interface Item {
  value: number | string
  name: string
}

interface Props {
  value?: string | number
  onChange: (value: string | number) => void
  options?: Item[]
}

const Select: FC<Props> = ({ value, onChange, options }) => {
  const currentValue = options?.find((i) => i.value === value)

  return (
    <Listbox value={value} onChange={onChange}>
      <div className="relative mt-1">
        <Listbox.Button className={s.select}>
          <span className="block truncate">{currentValue?.name}</span>
          <div className={s.selectBtn} />
        </Listbox.Button>
        <Transition
          as={Fragment}
          leave="transition ease-in duration-100"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <Listbox.Options className={s.options}>
            {options?.map((item) => (
              <Listbox.Option
                key={item.value}
                className={({ active }) => cn(s.option, { [s.optionActive]: active })}
                value={item.value}
              >
                {({ selected }) => (
                  <span className={`block truncate ${selected ? 'font-medium' : 'font-normal'}`}>
                    {item.name}
                  </span>
                )}
              </Listbox.Option>
            ))}
          </Listbox.Options>
        </Transition>
      </div>
    </Listbox>
  )
}

export default Select
