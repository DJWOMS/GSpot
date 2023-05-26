'use client'

import { Controller, useForm } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import { Input } from 'components/Form'
import Select from 'components/Select'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './CheckoutForm.module.css'

type FormType = {
  fullName: string
  email: string
  phoneNumber: string
  paymentMethod: 'visa' | 'mastercard' | 'qiwi'
}

const CheckoutForm = () => {
  const {
    handleSubmit,
    control,
    formState: { errors },
  } = useForm<FormType>()

  const onSubmitCheckout = async (data: FormType) => {
    const response = await fetchServerSide({
      path: '/profile/checkout',
      method: 'POST',
      body: JSON.stringify(data),
    })
    if (response) {
      console.log(response)
    }
  }

  return (
    <div>
      <form className={s.form} onSubmit={handleSubmit(onSubmitCheckout)}>
        <Controller
          control={control}
          name="fullName"
          defaultValue=""
          rules={{ required: true }}
          render={({ field }) => {
            return <Input {...field} type="text" placeholder="John Doe" />
          }}
        />
        <ErrorMessage errors={errors} name="fullName" render={({ message }) => <p>{message}</p>} />
        <Controller
          control={control}
          name="email"
          defaultValue=""
          rules={{ required: true }}
          render={({ field }) => {
            return <Input {...field} type="email" placeholder="gg@template.by" />
          }}
        />
        <ErrorMessage errors={errors} name="email" render={({ message }) => <p>{message}</p>} />
        <Controller
          control={control}
          name="phoneNumber"
          defaultValue=""
          rules={{ required: true }}
          render={({ field }) => {
            return <Input {...field} type="text" placeholder="+1 234 567-89-00" />
          }}
        />
        <ErrorMessage errors={errors} name="phoneNumber" render={({ message }) => <p>{message}</p>} />
        <Controller
          control={control}
          name="paymentMethod"
          defaultValue="visa"
          rules={{ required: true }}
          render={({ field }) => {
            return (
              <Select
                {...field}
                options={[
                  {
                    name: 'Visa',
                    value: 'visa',
                  },
                  {
                    name: 'Mastercard',
                    value: 'mastercard',
                  },
                  {
                    name: 'Qiwi',
                    value: 'qiwi',
                  },
                ]}
              />
            )
          }}
        />
        <ErrorMessage errors={errors} name="paymentMethod" render={({ message }) => <p>{message}</p>} />
        <span className={s.formText}>
          There are many variations of passages of Lorem Ipsum available, but the majority have suffered
          alteration in some form.
        </span>
        <input type="submit" className={s.formBtn} />
      </form>
    </div>
  )
}

export default CheckoutForm
