'use client'

import { SubmitHandler, useForm, Controller } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import { Input } from 'components/Form'
import Section from 'components/Section'
import { LINK_TO_GOOGLE_MAPS } from 'configs'
import { fetchServerSide } from 'lib/fetchServerSide'
import Link from 'next/link'
import s from './page.module.css'

interface FormProps {
  name: string
  email: string
  subject: string
  message: string
}

const ContactsPage = () => {
  const {
    register,
    control,
    reset,
    handleSubmit,
    formState: { errors },
  } = useForm<FormProps>()

  const onSubmit: SubmitHandler<FormProps> = async (data) => {
    const response = await fetchServerSide({
      path: '/contacts',
      method: 'POST',
      body: JSON.stringify(data),
    })
    if (response) {
      alert(JSON.stringify('Спасибо! Ваши данные успешно отправлены!'))
      reset()
    }
  }

  const rules = {
    required: 'The field is required',
    minLength: { value: 2, message: 'Please, enter more than 2 characters!' },
  }
  const rulesForEmail = {
    required: 'The field is required',
    pattern: { value: /[^@]+@[^.]+\..+/, message: 'Е-mail is invalid!' },
  }

  const disabled = !!errors.name || !!errors.email || !!errors.message || !!errors.subject

  return (
    <Section title="Contacts">
      <div className={s.row}>
        <div className={s.contactsForm}>
          <Section title="Contacts form" />
          <form className={s.form} action="#" onSubmit={handleSubmit(onSubmit)}>
            <Controller
              name="name"
              control={control}
              rules={rules}
              render={({ field }) => <Input {...field} type="text" placeholder="Name" />}
            />
            <ErrorMessage
              errors={errors}
              name="name"
              render={({ message }) => <p className={s.errorMessage}>{message}</p>}
            />

            <Controller
              name="email"
              control={control}
              rules={rulesForEmail}
              render={({ field }) => <Input {...field} type="text" placeholder="Email" />}
            />
            <ErrorMessage
              name="email"
              errors={errors}
              render={({ message }) => <p className={s.errorMessage}>{message}</p>}
            />

            <Controller
              name="subject"
              control={control}
              rules={rules}
              render={({ field }) => <Input {...field} type="text" placeholder="Subject" />}
            />
            <ErrorMessage
              name="subject"
              errors={errors}
              render={({ message }) => <p className={s.errorMessage}>{message}</p>}
            />

            <textarea
              className={s.formTextarea}
              placeholder="Type your message..."
              {...register('message', rules)}
            ></textarea>
            <ErrorMessage
              errors={errors}
              name="message"
              render={({ message }) => <p className={s.errorMessage}>{message}</p>}
            />

            <button className={s.formBtn} disabled={disabled}>
              Send
            </button>
          </form>
        </div>
        <Section title="Info">
          <div className={s.contacts}>
            <p>
              It is a long fact that a reader will be distracted by the readable content of a page when
              looking at its layout.
            </p>

            <ul className={s.list}>
              <li>
                <Link href="tel:+18092345678">+1 809 234-56-78</Link>
              </li>
              <li>
                <Link href="mailto:support@gg.template">support@gg.template</Link>
              </li>
              <li>
                <Link href={LINK_TO_GOOGLE_MAPS}>221B Baker St, Marylebone, London</Link>
              </li>
            </ul>
          </div>
        </Section>
      </div>
    </Section>
  )
}

export default ContactsPage
