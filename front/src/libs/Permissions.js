import store from '@/store'

function hasPermissions(value) {
    const permissions = store.state.auth.me.permissions || [];
    if(typeof value === 'string') {
        return permissions.includes(value);
    }
    if (Array.isArray(value)) {
        let hasPermission = false;
        for (let i = 0; i < value.length; i++) {
            const elPer = value[i];
            if (permissions.includes(elPer)) {
                hasPermission = true;
                break;
            }
        }
        return hasPermission
    }
}
export { hasPermissions };