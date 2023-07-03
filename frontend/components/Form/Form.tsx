import { useEffect } from 'react'
import { Controller, useForm } from 'react-hook-form'
import type { FieldValues, ControllerProps, UseFormProps, UseFormSetValue } from 'react-hook-form'
import type { UseControllerProps } from 'react-hook-form/dist/types/controller'
import { ErrorMessage } from '@hookform/error-message'
import s from './Form.module.css'

interface FieldType<T extends FieldValues> extends Pick<UseControllerProps<T>, 'name' | 'rules'> {
  label?: string
  render: ControllerProps<T>['render']
}

interface Props<T extends FieldValues> {
  fields: FieldType<T>[]
  title?: string
  onSubmit: (values: T) => void
  btnText: string
  config: UseFormProps<T>
  disabled?: boolean
  styleBtn?: string
  onResetButton?: boolean
  onResetSubmit?: boolean
  updateValueCallback?: (value: UseFormSetValue<T>) => void
}

function Form<T extends FieldValues>({
  fields,
  styleBtn = s.formBtn,
  title,
  disabled,
  onSubmit,
  btnText,
  config,
  updateValueCallback,
  onResetButton = false,
  onResetSubmit = false,
}: Props<T>) {
  const {
    control,
    handleSubmit,
    formState: { errors },
    reset,
    setValue,
  } = useForm<T>(config)

  useEffect(() => {
    if (updateValueCallback) {
      updateValueCallback(setValue)
    }
  }, [updateValueCallback, setValue])

  const onResetSubmitAction = (data: T) => {
    onSubmit(data)
    onResetSubmit && reset()
  }

  return (
    <form className={s.form} onSubmit={handleSubmit(onResetSubmitAction)}>
      {title && <h4 className={s.formTitle}>{title}</h4>}
      {onResetButton && (
        <button className={s.formButtonReset} type="button" onClick={() => reset()}>
          сбросить
        </button>
      )}
      <div className={s.col}>
        {fields.map(({ label, ...field }, index) => (
          <div key={`item-${index}`}>
            {label && (
              <label className={s.formLabel} htmlFor={field.name}>
                {label}
              </label>
            )}
            <Controller<T> control={control} {...field} />
            <ErrorMessage
              errors={errors}
              name={field.name as T['']}
              render={({ message }) => <p className={s.errorMessage}>{message}</p>}
            />
          </div>
        ))}
      </div>
      <button type="submit" className={styleBtn} disabled={disabled}>
        {btnText}
      </button>
    </form>
  )
}

export default Form
