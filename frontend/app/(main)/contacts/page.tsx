'use client'

import { SubmitHandler, useForm, Controller } from 'react-hook-form'
import { Input } from 'components/Form'
import Section from 'components/Section'
import { LINK_TO_GOOGLE_MAPS } from 'configs'
import { ContactsFormInterface } from 'features/contacts'
import { fetchServerSide } from 'lib/fetchServerSide'
import Link from 'next/link'
import s from './page.module.scss'

interface FormProps {
  name: string
  email: string
  subject: string
  message: string
}
const sendContacts = async () => {
  const contacts = await fetchServerSide<ContactsFormInterface[]>({
    path: '/contacts',
  })
  alert(JSON.stringify(contacts))
  console.log(contacts)
  return <ContactsPage />
}

const ContactsPage = () => {
  const {
    register,
    control,
    formState: { errors },
    reset,
    handleSubmit,
  } = useForm<FormProps>()

  const onSubmit: SubmitHandler<FormProps> = (data) => {
    console.log(data)
    reset()
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

  return (
    <Section title="Contacts">
      <div className={s.row}>
        <div className={s.contactsForm}>
          <Section title="Contacts form" />
          <form className={s.form} action="#" onSubmit={handleSubmit(onSubmit)}>
            <Controller name="name" control={control} rules={rules} render={({ field }) => <Input {...field} type="text" placeholder="Name" />} />
            <p className={s.errorMessage}>{errors.name && errors.name.message}</p>

            <Controller
              name="email"
              control={control}
              rules={rulesForEmail}
              render={({ field }) => <Input {...field} type="text" placeholder="Email" />}
            />
            <p className={s.errorMessage}>{errors.email && errors.email.message}</p>

            <Controller
              name="subject"
              control={control}
              rules={rules}
              render={({ field }) => <Input {...field} type="text" placeholder="Subject" />}
            />
            <p className={s.errorMessage}>{errors.subject && errors.subject.message}</p>
            <textarea className={s.formTextarea} placeholder="Type your message..." {...register('message', rules)}></textarea>
            <p className={s.errorMessage}>{errors.message && errors.message.message}</p>

            <button className={s.formBtn} onClick={sendContacts} disabled={disabled}>
              Send
            </button>
          </form>
        </div>
        <Section title="Info">
          <div className={s.contacts}>
            <p>It is a long fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>

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
