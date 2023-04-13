'use client'

import { FC } from 'react'
import { SubmitHandler, useForm, Controller } from 'react-hook-form'
import { Input } from 'components/Form'
import Section from 'components/Section'
import Link from 'next/link'
import s from './page.module.scss'

interface FormProps {
  name: string
  email: string
  subject: string
  message: string
}

const ContactsPage: FC<FormProps> = () => {
  const {
    control,
    formState: { errors },
    reset,
    handleSubmit,
  } = useForm<FormProps>()

  const onSubmit: SubmitHandler<FormProps> = (data) => {
    alert(JSON.stringify(data))
    console.log(data)
    reset({ name: '', email: '', message: '', subject: '' })
  }

  const rules = {
    required: true,
    minLength: { value: 2, message: 'Please, enter more than 2 characters!' },
  }
  const rulesForEmail = {
    required: true,
    pattern: { value: /[^@]+@[^.]+\..+/, message: 'Е-mail is invalid!' },
  }

  const disabled = !!errors.name || !!errors.email || !!errors.message || !!errors.subject

  const linkMap =
    'https://maps.google.com/maps?q=221B+Baker+Street,+London,+United+Kingdom&amp;hl=en&amp;t=v&amp;hnear=221B+Baker+St,+London+NW1+6XE,+United+Kingdom'

  return (
    <Section title="Contacts">
      <div className={s.row}>
        <div className={s.contactsForm}>
          <Section title="Contacts form" />
          <form className={s.form} action="#" onSubmit={handleSubmit(onSubmit)}>
            <Controller name="name" control={control} rules={rules} render={({ field }) => <Input {...field} type="text" placeholder="Name" />} />
            {errors.name ? <p className={s.errorMessage}>{errors.name.message}</p> : <p className={s.emptyBlock}></p>}

            <Controller
              name="email"
              control={control}
              rules={rulesForEmail}
              render={({ field }) => <Input {...field} type="text" placeholder="Email" />}
            />
            {errors.email ? <p className={s.errorMessage}>{errors.email.message}</p> : <p className={s.emptyBlock}></p>}

            <Controller
              name="subject"
              control={control}
              rules={rules}
              render={({ field }) => <Input {...field} type="text" placeholder="Subject" />}
            />
            {errors.subject ? <p className={s.errorMessage}>{errors.subject.message}</p> : <p className={s.emptyBlock}></p>}

            <Controller
              name="message"
              control={control}
              rules={rules}
              render={({ field }) => <textarea className={s.formTextarea} {...field} placeholder="Type your message..." />}
            />
            {errors.message ? <p className={s.errorMessage}>{errors.message.message}</p> : <p className={s.emptyBlock}></p>}

            <button className={s.formBtn} disabled={disabled}>
              Send
            </button>
          </form>
        </div>
        <Section title="Info">
          <div className={s.contactsInfo}>
            <p className={s.contacts}>
              It is a long fact that a reader will be distracted by the readable content of a page when looking at its layout.
            </p>

            <ul>
              <li className={s.contactsList}>
                <Link href="tel:+18092345678">+1 809 234-56-78</Link>
              </li>

              <li className={s.contactsList}>
                <Link href="mailto:support@gg.template">support@gg.template</Link>
              </li>

              <li className={s.contactsList}>
                <Link href={linkMap}>221B Baker St, Marylebone, London</Link>
              </li>
            </ul>
          </div>
        </Section>
      </div>
    </Section>
  )
}

export default ContactsPage
