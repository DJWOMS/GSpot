'use client'

import Link from 'next/link'

import { IconBrandFacebook, IconBrandGoogle, IconBrandTwitter } from '@tabler/icons-react'
import { Form, SignCheckbox, SignGroup, SignInput, SignBtn, SignDelimiter, SignSocial, SignSocials, SignText } from '../Form'

export default function Signup() {
    return (
        <Form onSubmit={() => console.log('hello')}>
            <SignGroup>
                <SignInput type="text" placeholder="Введите username" />
            </SignGroup>

            <SignGroup>
                <SignInput type="email" placeholder="Введите email" />
            </SignGroup>

            <SignGroup>
                <SignInput type="password" placeholder="Введите пароль" />
            </SignGroup>

            <SignCheckbox>
                <input id="agree" />
                <label htmlFor="agree">Я подтверждаю правила</label>
            </SignCheckbox>

            <SignBtn>Регистрация</SignBtn>
            <SignDelimiter>или</SignDelimiter>

            <SignSocials>
                <SignSocial color="fb">
                    <IconBrandFacebook />
                </SignSocial>

                <SignSocial color="gl">
                    <IconBrandGoogle />
                </SignSocial>

                <SignSocial color="tw">
                    <IconBrandTwitter />
                </SignSocial>
            </SignSocials>

            <SignText>
                Уже есть аккаунт? <Link href="/signin">Авторизация</Link>
            </SignText>
        </Form>
    )
}
