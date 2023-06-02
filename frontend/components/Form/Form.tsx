import { Controller, useForm } from 'react-hook-form'
import type { FieldValues, Path, ControllerProps, RegisterOptions, UseFormProps } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import s from './Form.module.css'

interface FieldType<T extends FieldValues> {
  name: Path<T>
  label: string
  rules?: Exclude<RegisterOptions, 'valueAsNumber' | 'valueAsDate' | 'setValueAs'>
  render: ControllerProps<T>['render']
}

interface Props<T extends FieldValues> {
  fields: FieldType<T>[]
  title?: string
  onSubmit: (values: T) => void
  btnText: string
  config: UseFormProps<T>
  onResetButton?: boolean
  onResetSubmit?: boolean
}

function Form<T extends FieldValues>({
  fields,
  title,
  onSubmit,
  btnText,
  config,
  onResetButton = false,
  onResetSubmit = false,
}: Props<T>) {
  const {
    control,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<T>(config)

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
            <label className={s.formLabel} htmlFor={field.name}>
              {label}
            </label>
            <Controller<T> control={control} {...field} />
            <ErrorMessage
              errors={errors}
              name={field.name as T['name']}
              render={({ message }) => <p className={s.errorMessage}>{message}</p>}
            />
          </div>
        ))}
      </div>
      <button type="submit" className={s.formBtn}>
        {btnText}
      </button>
    </form>
  )
}

export default Form
